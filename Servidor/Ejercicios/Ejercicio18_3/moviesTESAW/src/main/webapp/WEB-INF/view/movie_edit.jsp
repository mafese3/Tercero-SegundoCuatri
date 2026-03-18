<%@ page import="java.util.List" %>
<%@ page import="es.tesaw.movies.entity.MovieEntity" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Lista de películas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<h1>Lista de película</h1>

<%
    MovieEntity peli = (MovieEntity) request.getAttribute("pelicula");
%>

<form action="" method="get">
    <table class="table table-striped table-bordered table-hover align-middle">
        <tr>
            <th>TITLE</th>
            <th>BUDGET</th>
            <th>RATING</th>
            <th>DURATION</th>
            <th>PLOT</th>
            <th>RELEASE DATE</th>
        </tr>
        <tr>

            <td><input type="text" value="<%=peli.getTitle()%>" name="titulo"></td>
            <td><input type="number" value="<%= peli.getBudget() %>" name="presupuesto"> </td>
            <td><input type="number" value="<%= peli.getVoteAverage() %>" name="valoracion"> </td>
            <td><input type="number" value="<%= peli.getRuntime() %>" name="duracion"> </td>
            <td><textarea class=""><%= peli.getOverview() %></textarea> </td>
            <td><input type="date" value="<%= peli.getReleaseDate() %>" name="fecha"> </td>
        </tr>

    </table>
</form>

</body>
</html>
