<%@ page import="es.tesaw.movies.entity.Movies" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<%
    List<Movies> peliculas = (List<Movies>) request.getAttribute("pelis");
%>

<body>
<h1>Lista de películas</h1>
<table>
    <thead>
        <tr>
            <th>TITULO</th>
            <th>BUDGET</th>
            <th>RATING</th>
            <th>DURATION</th>
        </tr>
    </thead>


<%
    for (Movies peli: peliculas) {
%>
    <tr>
        <td><%=peli.getTitle()%></td>
        <td><%=peli.getBudget()%></td>
        <td><%=peli.getVoteAverage()%></td>
        <td><%=peli.getRuntime()%></td>
    </tr>



<%
    }
%>

</table>


</body>
</html>
