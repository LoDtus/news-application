package com.statistic.statistic_service.model.entity;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class EmailEvent {
    private String action;
    private Email email;

    public EmailEvent(String action, Email email) {
        this.action = action;
        this.email = email;
    }
    public EmailEvent() {}

    @Override
    public String toString() {
        return "EmailEvent{" +
                "action='" + action + '\'' +
                ", email=" + email +
                '}';
    }
}
