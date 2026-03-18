package es.tesaw.movies.dao;

import es.tesaw.movies.entity.MovieEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MoviesRepository extends JpaRepository<MovieEntity, Integer> {
}
