package com.notification.notification_service.service;

import com.notification.notification_service.model.entity.Message;
import java.util.List;

public interface MessageService {
    List<Message> findAll();
    Message findById(int theId);
    Message save(Message theMessage);
    void deleteById(int theId);
}