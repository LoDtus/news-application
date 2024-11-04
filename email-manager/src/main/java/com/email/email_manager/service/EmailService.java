package com.email.email_manager.service;

import com.email.email_manager.model.entity.Email;
import org.springframework.data.domain.Pageable;

import java.util.List;

public interface EmailService {
    List<Email> findAll();
    Email findById(int theId);
    Email save(Email theEmail);
    void deleteById(int theId);
}
