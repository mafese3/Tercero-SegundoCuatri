package es.tesaw.movies.dao;

import es.tesaw.movies.entity.Movies;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MoviesRepository extends JpaRepository<Movies, Long>{
    
}
