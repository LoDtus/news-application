package com.email.email_manager.service;

import com.email.email_manager.model.dao.EmailRepository;
import com.email.email_manager.model.entity.Email;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class EmailServiceImpl implements EmailService {
    private final EmailRepository emailRepository;

    @Autowired
    public EmailServiceImpl(EmailRepository emailRepository) {
        this.emailRepository = emailRepository;
    }

    @Override
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public List<Email> findAll() {
        return emailRepository.findAll();
    }

    @Override
    @PreAuthorize("hasRole('ROLE_ADMIN')")
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
    public Email save(Email theEmail) {
        return emailRepository.save(theEmail);
    }

    @Override
    @PreAuthorize("hasRole('ROLE_ADMIN')")
    public void deleteById(int theId) {
        emailRepository.deleteById(theId);
    }
}
