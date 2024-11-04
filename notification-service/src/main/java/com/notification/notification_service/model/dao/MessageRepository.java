package com.notification.notification_service.model.dao;

import com.notification.notification_service.model.entity.Message;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MessageRepository extends JpaRepository<Message, Integer> {
}
