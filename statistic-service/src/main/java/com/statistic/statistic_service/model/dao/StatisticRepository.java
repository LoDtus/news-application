package com.statistic.statistic_service.model.dao;

import com.statistic.statistic_service.model.entity.Statistic;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StatisticRepository extends JpaRepository<Statistic, Integer> {
}
