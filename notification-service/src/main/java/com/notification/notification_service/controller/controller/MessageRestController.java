package com.notification.notification_service.controller.controller;

import com.notification.notification_service.model.entity.Message;
import com.notification.notification_service.service.MessageService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class MessageRestController {
    private MessageService messageService;
    public MessageRestController(MessageService messageService) {
        this.messageService = messageService;
    }

    @GetMapping("/messages")
    public List<Message> findAll() {
        return messageService.findAll();
    }

    @GetMapping("/messages/{messageId}")
    public Message getMessage(@PathVariable int messageId) {
        Message theMessage = messageService.findById(messageId);
        if (theMessage == null) {
            throw new RuntimeException("Message id not found - " + messageId);
        }
        return theMessage;
    }

    @PostMapping("/messages")
    public Message sendMessage(@RequestBody Message theMessage) {
        theMessage.setId(0);
        Message dbMessage = messageService.save(theMessage);
        return dbMessage;
    }

    @DeleteMapping("/messages/{messageId}")
    public String deleteMessage(@PathVariable int messageId) {
        Message tempMessage = messageService.findById(messageId);
        if (tempMessage == null) {
            throw new RuntimeException("Message id not found - " + messageId);
        }
        messageService.deleteById(messageId);
        return "Deleted message id - " + messageId;
    }
}
