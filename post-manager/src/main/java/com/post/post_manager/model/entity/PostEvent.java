package com.post.post_manager.model.entity;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PostEvent {
    private String action;
    private Post post;

    public PostEvent(String action, Post post) {
        this.action = action;
        this.post = post;
    }
    public PostEvent() {}

    @Override
    public String toString() {
        return "PostEvent{" +
                "action='" + action + '\'' +
                ", post=" + post +
                '}';
    }
}
