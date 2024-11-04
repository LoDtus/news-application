package com.notification.notification_service.model.entity;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@Entity
@Table(name = "posts")
public class Post {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @Column(name = "title")
    private String title;

    @Column(name = "thumbnail")
    private String thumbnail;

    @Column(name = "content")
    private String content;

    @Column(name = "creation_date")
    private LocalDateTime creationDate;

    @Column(name = "is_show")
    private int show;

    public Post(String title, String thumbnail, String content, LocalDateTime creationDate, int show) {
        this.title = title;
        this.thumbnail = thumbnail;
        this.content = content;
        this.creationDate = creationDate;
        this.show = show;
    }
    public Post() {}

    @Override
    public String toString() {
        return "Post{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", thumbnail='" + thumbnail + '\'' +
                ", content='" + content + '\'' +
                ", creationDate=" + creationDate +
                ", show=" + show +
                '}';
    }
}
