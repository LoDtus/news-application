package com.email.email_manager;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class EmailManagerApplication {

	public static void main(String[] args) {
		SpringApplication.run(EmailManagerApplication.class, args);
	}
	@Bean
	NewTopic notification() {
		return new NewTopic("notification-email", 2, (short) 3);
	}
}
