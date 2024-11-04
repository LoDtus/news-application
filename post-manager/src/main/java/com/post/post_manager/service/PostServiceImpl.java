package com.post.post_manager.service;

import com.post.post_manager.model.dao.PostRepository;
import com.post.post_manager.model.entity.Post;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PostServiceImpl implements PostService {
    private PostRepository postRepository;

    @Autowired
    public PostServiceImpl(PostRepository postRepository) {
        this.postRepository = postRepository;
    }

    @Override
    public List<Post> findAll() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        String role = authentication.getAuthorities().iterator().next().getAuthority();

        if (role.equals("ROLE_ADMIN")) {
            return postRepository.findAll();
        } else if (role.equals("ROLE_USER")) {
            return postRepository.findAllByShow(1);
        } else {
            throw new AccessDeniedException("Access denied");
        }
    }

    @Override
    public Post findById(int theId) {
        Optional<Post> result = postRepository.findById(theId);
        Post thePost = null;
        if (result.isPresent()) {
            thePost = result.get();
        } else {
            throw new RuntimeException("Did not find post id - " + theId);
        }
        return thePost;
    }

    @Override
    public Post save(Post thePost) {
        return postRepository.save(thePost);
    }

    @Override
    public void deleteById(int theId) {
        postRepository.deleteById(theId);
    }
}
