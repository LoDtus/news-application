package com.statistic.statistic_service.model.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "statistic")
public class Statistic {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "total_post")
    private int totalPost;

    @Column(name = "total_post_show")
    private int totalPost_show;

    @Column(name = "total_post_hidden")
    private int totalPost_hidden;

    @Column(name = "total_email")
    private int totalEmail;

    public Statistic(int totalPost, int totalPost_show, int totalPost_hidden, int totalEmail) {
        this.totalPost = totalPost;
        this.totalPost_show = totalPost_show;
        this.totalPost_hidden = totalPost_hidden;
        this.totalEmail = totalEmail;
    }
    public Statistic() {}

    @Override
    public String toString() {
        return "Statistic{" +
                "id=" + id +
                ", totalPost=" + totalPost +
                ", totalPost_show=" + totalPost_show +
                ", totalPost_hidden=" + totalPost_hidden +
                ", totalEmail=" + totalEmail +
                '}';
    }
}
