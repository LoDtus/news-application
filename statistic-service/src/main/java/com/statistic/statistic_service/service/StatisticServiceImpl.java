package com.statistic.statistic_service.service;

import com.statistic.statistic_service.model.dao.StatisticRepository;
import com.statistic.statistic_service.model.entity.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class StatisticServiceImpl implements StatisticService {
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    private final StatisticRepository statisticRepository;

    @Autowired
    public StatisticServiceImpl(StatisticRepository statisticRepository) {
        this.statisticRepository = statisticRepository;
    }

    @Override
    public List<Statistic> findAll() {
        return statisticRepository.findAll();
    }

    @Override
    public Statistic save(Statistic statistic) {
        return statisticRepository.save(statistic);
    }

    @KafkaListener(id = "statisticPostGroup", topics = "notification-post")
    public void listenPost(PostEvent postEvent) {
        String action = postEvent.getAction();
        Post thePost = postEvent.getPost();
        System.out.println("\n\nPost\n\n");

        List<Statistic> listStatistic = findAll();
        Statistic statistic = listStatistic.getFirst();

        if ("POST".equals(action)) {
            statistic.setTotalPost(statistic.getTotalPost() + 1);
            if (thePost.getShow() == 1) {
                statistic.setTotalPost_show(statistic.getTotalPost_show() + 1);
            } else {
                statistic.setTotalPost_hidden(statistic.getTotalPost_hidden() + 1);
            }
        } else if ("DELETE".equals(action)) {
            statistic.setTotalPost(statistic.getTotalPost() - 1);
            if (thePost.getShow() == 1) {
                statistic.setTotalPost_show(statistic.getTotalPost_show() - 1);
            } else {
                statistic.setTotalPost_hidden(statistic.getTotalPost_hidden() - 1);
            }
        }
        save(statistic);
    }

    @KafkaListener(id = "statisticEmailGroup", topics = "notification-email")
    public void listenEmail(EmailEvent emailEvent) {
        String action = emailEvent.getAction();
        Email theEmail = emailEvent.getEmail();
        List<Statistic> listStatistic = findAll();
        Statistic statistic = listStatistic.getFirst();
        System.out.println("\n\nEmail\n\n");

        if ("POST".equals(action)) {
            statistic.setTotalEmail(statistic.getTotalEmail() + 1);
        } else if ("DELETE".equals(action)) {
            statistic.setTotalEmail(statistic.getTotalEmail() - 1);
        }
        save(statistic);
    }
}
