package com.post.post_manager.controller.controller;

import com.post.post_manager.model.entity.Post;
import com.post.post_manager.model.entity.PostEvent;
import com.post.post_manager.service.PostService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class PostRestController {
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    private PostService postService;
    public PostRestController(PostService postService) {
        this.postService = postService;
    }

    @GetMapping("/posts")
    public List<Post> findAll() {
        return postService.findAll();
    }

    @GetMapping("/posts/{postId}")
    public Post getPost(@PathVariable int postId) {
        Post thePost = postService.findById(postId);
        if (thePost == null) {
            throw new RuntimeException("Post id not found - " + postId);
        }
        return thePost;
    }

    @Autowired
    KafkaTemplate<String, Object> kafkaTemplate;

    @PostMapping("/posts")
    public Post addPost(@RequestBody Post thePost) {
        thePost.setId(0);
        Post dbPost = postService.save(thePost);

        PostEvent postEvent = new PostEvent("POST", dbPost);
        kafkaTemplate.send("notification-post", postEvent);
        return dbPost;
    }

    @PutMapping("/posts")
    public Post updatePost(@RequestBody Post thePost) {
        Post dbPost = postService.save(thePost);
        return dbPost;
    }

    @DeleteMapping("/posts/{postId}")
    public String deletePost(@PathVariable int postId) {
        Post dbPost = postService.findById(postId);
        if (dbPost == null) {
            throw new RuntimeException("Post id not found - " + postId);
        }

        PostEvent postEvent = new PostEvent("DELETE", dbPost);
        kafkaTemplate.send("notification-post", postEvent);
        postService.deleteById(postId);
        return "Deleted post id - " + postId;
    }
}