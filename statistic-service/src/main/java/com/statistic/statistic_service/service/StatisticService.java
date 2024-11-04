package com.statistic.statistic_service.service;

import com.statistic.statistic_service.model.entity.Statistic;

import java.util.List;

public interface StatisticService {
    List<Statistic> findAll();
    Statistic save(Statistic statistic);
}
