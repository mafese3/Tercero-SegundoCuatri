package es.uma.tesaw.demo2026.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class Controlador {
    @GetMapping("/inicio")
    public String doInicio() {
        return "prueba.html";
    }

    @GetMapping("/login")
    public String doLogin(@RequestParam("user") String usuario,
                          @RequestParam("pwd") String contrasenia,
                          Model model) {
        String respuesta = "";
        if (usuario.equals(contrasenia)) {
            respuesta = "son iguales";
        } else {
            respuesta = "no son iguales";
        }

        model.addAttribute("respuesta", respuesta);
        return "prueba.jsp";
    }
}