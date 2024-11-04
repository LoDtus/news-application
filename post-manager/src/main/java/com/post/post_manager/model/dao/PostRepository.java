package com.post.post_manager.model.dao;

import com.post.post_manager.model.entity.Post;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PostRepository extends JpaRepository<Post, Integer> {
    List<Post> findAllByShow(int show);
}