package com.notification.notification_service.service;

import com.notification.notification_service.model.dao.EmailRepository;
import com.notification.notification_service.model.entity.Email;
import com.notification.notification_service.model.entity.Message;
import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.scheduling.annotation.Async;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;
import org.thymeleaf.context.Context;
import org.thymeleaf.spring6.SpringTemplateEngine;

import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class EmailSeviceImpl implements EmailService {
    private EmailRepository emailRepository;
    Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private JavaMailSender javaMailSender;

    @Autowired
    private SpringTemplateEngine templateEngine;

    @Value("${spring.mail.username}")
    private String sender;

    @Autowired
    public EmailSeviceImpl(EmailRepository emailRepository) {
        this.emailRepository = emailRepository;
    }

    @Override
    public List<Email> findAll() {
        return emailRepository.findAll();
    }

    @Override
    public Email findById(int theId) {
        Optional<Email> result = emailRepository.findById(theId);
        Email theEmail = null;
        if (result.isPresent()) {
            theEmail = result.get();
        } else {
            throw new RuntimeException("Did not find email id - " + theId);
        }
        return theEmail;
    }

    @Override
    public List<Integer> getAllEmailId() {
        List<Email> allEmails = findAll();
        return allEmails.stream()
                .map(Email::getId)
                .collect(Collectors.toList());
    }

    @Async
    @Override
    public void sendMessage(Message theMessage) {
        try {
            logger.info("Start... Sending email");

            List<Integer> idReceiverList = theMessage.getIdReceiver();
            for (Integer receiverId : idReceiverList) {
                Email theEmail = findById(receiverId);

                if (theEmail != null && !theEmail.getEmail().trim().isEmpty()) {
                    MimeMessage message = javaMailSender.createMimeMessage();
                    MimeMessageHelper helper = new MimeMessageHelper(message, StandardCharsets.UTF_8.name());

                    // Load template Email:
                    Context context = new Context();
                    context.setVariable("content", theMessage.getContent());
                    context.setVariable("author", theMessage.getAuthor());
                    String html = templateEngine.process("notification-email", context);

                    // Send Email:
                    helper.setTo(theEmail.getEmail());
                    helper.setText(html, true);
                    helper.setSubject(theMessage.getSubject());
                    helper.setFrom(sender);
                    javaMailSender.send(message);
                    logger.info("End... Email sent success!");
                } else {
                    logger.warn("No receivers found for this message!");
                }
            }
        } catch (MessagingException exc) {
            logger.error("Email sent with error: " + exc.getMessage());
        }
    }
}
