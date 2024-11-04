package com.statistic.statistic_service.model.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@Entity
@Table(name = "emails")
public class Email {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "email")
    private String email;

    @Column(name = "join_date")
    private LocalDateTime joinDate;

    public Email(String email, LocalDateTime joinDate) {
        this.email = email;
        this.joinDate = joinDate;
    }
    public Email() {}

    @Override
    public String toString() {
        return "Email{" +
                "id=" + id +
                ", email='" + email + '\'' +
                ", joinDate='" + joinDate + '\'' +
                '}';
    }
}