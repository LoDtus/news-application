package com.notification.notification_service.model.entity;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Set;

@Getter
@Setter
@Entity
@Table(name = "messages")
public class Message {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private int id;

    @OneToOne
    @JoinColumn(name = "id_post")
    private Post post;

    @Column(name = "send_date")
    private LocalDateTime sendDate;

    @Column(name = "subject")
    private String subject;

    @Column(name = "content")
    private String content;

    @Column(name = "author")
    private String author;

    @Column(name = "id_receiver", columnDefinition = "JSON")
    private String idReceiverJson;

    @Transient
    private List<Integer> idReceiver;

    public Message(Post post, LocalDateTime sendDate, String subject, String content, String author, String idReceiverJson, List<Integer> idReceiver) {
        this.post = post;
        this.sendDate = sendDate;
        this.subject = subject;
        this.content = content;
        this.author = author;
        this.idReceiverJson = idReceiverJson;
        this.idReceiver = idReceiver;
    }

    public Message() {}

    public List<Integer> getIdReceiver() {
        if (this.idReceiver == null && this.idReceiverJson != null) {
            ObjectMapper objectMapper = new ObjectMapper();
            try {
                this.idReceiver = objectMapper.readValue(this.idReceiverJson, new TypeReference<List<Integer>>() {});
            } catch (IOException exc) {
                exc.printStackTrace();
            }
        }
        return idReceiver;
    }

    public void setIdReceiver(List<Integer> idReceiver) {
        this.idReceiver = idReceiver;
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            this.idReceiverJson = objectMapper.writeValueAsString(idReceiver);
        } catch (IOException exc) {
            exc.printStackTrace();
        }
    }

    @Override
    public String toString() {
        return "Message{" +
                "id=" + id +
                ", post=" + post +
                ", sendDate=" + sendDate +
                ", subject='" + subject + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", idReceiverJson='" + idReceiverJson + '\'' +
                ", idReceiver=" + idReceiver +
                '}';
    }
}
