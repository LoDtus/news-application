package com.statistic.statistic_service.controller.controller;

import com.statistic.statistic_service.model.entity.Statistic;
import com.statistic.statistic_service.service.StatisticService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class StatisticRestController {
    private final StatisticService statisticService;
    public StatisticRestController(StatisticService statisticService) {
        this.statisticService = statisticService;
    }

    @GetMapping("/statistic")
    public List<Statistic> findAll() {
        return statisticService.findAll();
    }

    @PutMapping("/statistic")
    public Statistic updateStatistic(@RequestBody Statistic statistic) {
        Statistic dbStatistic = statisticService.save(statistic);
        return dbStatistic;
    }
}
