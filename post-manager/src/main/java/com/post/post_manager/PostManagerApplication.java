package com.post.post_manager;

import org.apache.kafka.clients.admin.NewTopic;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class PostManagerApplication {
	public static void main(String[] args) {
		SpringApplication.run(PostManagerApplication.class, args);
	}
	@Bean
	NewTopic notification() {
		return new NewTopic("notification-post", 2, (short) 3);
	}
}