package com.notification.notification_service.service;

import com.notification.notification_service.model.dao.MessageRepository;
import com.notification.notification_service.model.entity.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class MessageServiceImpl implements MessageService {
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    private MessageRepository messageRepository;

    @Autowired
    private EmailService emailService;

    @Autowired
    public MessageServiceImpl(MessageRepository messageRepository) {
        this.messageRepository = messageRepository;
    }

    @Override
    public List<Message> findAll() {
        return messageRepository.findAll();
    }

    @Override
    public Message findById(int theId) {
        Optional<Message> result = messageRepository.findById(theId);
        Message theMessage = null;
        if (result.isPresent()) {
            theMessage = result.get();
        } else {
            throw new RuntimeException("Did not find message id - " + theId);
        }
        return theMessage;
    }

    @Override
    public Message save(Message theMessage) {
        emailService.sendMessage(theMessage);
        return messageRepository.save(theMessage);
    }

    @Override
    public void deleteById(int theId) {
        messageRepository.deleteById(theId);
    }

    @KafkaListener(id = "notificationPostGroup", topics = "notification-post")
    public void listenPost(PostEvent postEvent) {
        String action = postEvent.getAction();
        Post thePost = postEvent.getPost();

        if ("POST".equals(action)) {
            Message theMessage = new Message();
            theMessage.setId(0);
            theMessage.setPost(thePost);
            theMessage.setSendDate(LocalDateTime.now());
            theMessage.setSubject("New Article Published on Breaking News!");
            theMessage.setContent("I hope this email finds you well.<br>" +
                    "I am pleased to inform you that a new article has just been published on our Breaking News. We encourage you to take a moment to read it and share your thoughts.<br>" +
                    "Thank you for your continued support!");
            theMessage.setAuthor("Breaking News");

            List<Integer> listId = emailService.getAllEmailId();
            theMessage.setIdReceiver(listId);
            save(theMessage);
        }
    }

    @KafkaListener(id = "notificationEmailGroup", topics = "notification-email")
    public void listenEmail(EmailEvent emailEvent) {
        String action = emailEvent.getAction();
        Email theEmail = emailEvent.getEmail();

        if ("POST".equals(action)) {
            Message theMessage = new Message();
            theMessage.setId(0);
            theMessage.setPost(null);
            theMessage.setSendDate(LocalDateTime.now());
            theMessage.setSubject("Welcome to Breaking News!");
            theMessage.setContent("Welcome to Breaking News – your go-to source for the latest and most reliable updates from around the world! We're excited to have you as part of our community.<br>" +
                    "If you have any questions or need help, don’t hesitate to reach out. We're here to ensure you have the best experience.");
            theMessage.setAuthor("Breaking News");
            theMessage.setIdReceiver(List.of(theEmail.getId()));
            save(theMessage);
        }
    }
}
