package com.notification.notification_service.service;

import com.notification.notification_service.model.entity.Email;
import com.notification.notification_service.model.entity.Message;
import java.util.List;

public interface EmailService {
    List<Email> findAll();
    Email findById(int theId);
    List<Integer> getAllEmailId();
    void sendMessage(Message theMessage);
}
