package es.tesaw.movies.controller;

import es.tesaw.movies.dao.MoviesRepository;
import es.tesaw.movies.entity.MovieEntity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class MoviesController {

    @Autowired
    protected MoviesRepository moviesRepository;



    @GetMapping("/")
    public String doInit (Model model) {

        List<MovieEntity> pelis = this.moviesRepository.findAll();
        model.addAttribute("pelis", pelis);
        return "movies";
    }

    @GetMapping("/editar")
    public String doeditar (@RequestParam("id") Integer id, Model model) {
        MovieEntity pelicula = this.moviesRepository.findById(id).get();
        model.addAttribute("pelicula", pelicula);
        return "movie_edit";
    }
}
