package com.notification.notification_service.model.dao;

import com.notification.notification_service.model.entity.Email;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmailRepository extends JpaRepository<Email, Integer> {
}
