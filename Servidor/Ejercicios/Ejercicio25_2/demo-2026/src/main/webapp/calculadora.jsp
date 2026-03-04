<%@ page import="org.apache.coyote.Request" %><%--
  Created by IntelliJ IDEA.
  User: marin
  Date: 02/03/2026
  Time: 11:21
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <%
        String mensaje = (String) request.getAttribute("error");
        if (mensaje != null && !mensaje.equals("")) {
    %>

    <h2>Se ha producido un error: <%= mensaje%></h2>

    <%
        }
    %>
    <form action="/calcular" method="post">
        <fieldset>
            <p>
                <label for="op1">Operador 1:</label>
                <input type="text" name="op1" id="op1" value=${resultado}>
            </p>

            <p>
                <label for="op2">Operador 2:</label>
                <input type="text" name="op2">
            </p>
        </fieldset>

            <input type="radio" name="operador" value="0"> +
            <input type="radio" name="operador" value="1">-
            <input type="radio" name="operador" value="2">*
            <input type="radio" name="operador" value="3">/

        <button>Operar</button>
    </form>

    <h1>El resultado es: </h1>
    ${resultado}
</body>
</html>
