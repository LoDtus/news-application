package com.email.email_manager.controller.controller;

import com.email.email_manager.model.entity.Email;
import com.email.email_manager.model.entity.EmailEvent;
import com.email.email_manager.service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class EmailRestController {
    private final EmailService emailService;
    public EmailRestController(EmailService emailService) {
        this.emailService = emailService;
    }

    @GetMapping("/emails")
    public List<Email> findAll() {
        return emailService.findAll();
    }

    @GetMapping("/emails/{emailId}")
    public Email getEmail(@PathVariable int emailId) {
        Email theEmail = emailService.findById(emailId);
        if (theEmail == null) {
            throw new RuntimeException("Email id not found - " + emailId);
        }
        return theEmail;
    }

    @Autowired
    KafkaTemplate<String, Object> kafkaTemplate;

    @PostMapping("/emails")
    public Email addEmail(@RequestBody Email theEmail) {
        theEmail.setId(0);
        Email dbEmail = emailService.save(theEmail);

        EmailEvent emailEvent = new EmailEvent("POST", dbEmail);
        kafkaTemplate.send("notification-email", emailEvent);
        return dbEmail;
    }

    @DeleteMapping("/emails/{emailId}")
    public String deleteEmail(@PathVariable int emailId) {
        Email dbEmail = emailService.findById(emailId);
        if (dbEmail == null) {
            throw new RuntimeException("Email id not found - " + emailId);
        }

        EmailEvent emailEvent = new EmailEvent("DELETE", dbEmail);
        kafkaTemplate.send("notification-email", emailEvent);
        emailService.deleteById(emailId);
        return "Deleted email id - " + emailId;
    }
}
