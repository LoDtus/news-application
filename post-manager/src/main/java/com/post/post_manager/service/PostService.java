package com.post.post_manager.service;

import com.post.post_manager.model.entity.Post;
import java.util.List;

public interface PostService {
    List<Post> findAll();
    Post findById(int theId);
    Post save(Post thePost);
    void deleteById(int theId);
}