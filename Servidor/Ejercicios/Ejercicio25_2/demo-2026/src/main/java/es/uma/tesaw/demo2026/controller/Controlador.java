package es.uma.tesaw.demo2026.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class Controlador {

    @GetMapping("/")
    public String doInicio () {
        return "login.html";

    }

    @PostMapping("/login")
    public String doLogin (@RequestParam("user") String usuario,
                           @RequestParam("pwd") String contrasenia,
                           Model model) {
        String respuesta = "";
        if (usuario.equals(contrasenia)) {
            respuesta = "Son iguales!!!";
        } else {
            respuesta = "No son iguales!!!";
        }

        model.addAttribute("respuesta", respuesta);

        return "prueba.jsp";
    }

    @GetMapping("/calculator")
    public String doCalculator (@RequestParam("a") int a, @RequestParam("b") int b, @RequestParam("op") String op, Model model) {
        double resultado = 0;

        if (op.equals("suma")) {
            resultado = a + b;
        } else if (op.equals("resta")) {
            resultado = a - b;
        } else if (op.equals("mult")) {
            resultado = a * b;
        } else if (op.equals("div")) {
            resultado = a / b;
        }

        model.addAttribute("resultado", resultado);

        return "resultado.jsp";
    }

    @PostMapping("/calcular")
    public String doCalcular (@RequestParam("op1") Float a, @RequestParam("op2") Float b, @RequestParam("operador") Integer operacion, Model model) {
        Float resultado = (float) 0;
        String error = "";
        switch (operacion) {
            case 0:
                resultado = a+b;
                break;
            case 1:
                resultado = a-b;
                break;
            case 2:
                resultado=a*b;
                break;
            case 3:
                if(b == 0 ){
                    error = "No se puede dividir por 0";
                } else{
                    resultado=a/b;
                }
                break;
        }

        model.addAttribute("resultado", resultado);
        model.addAttribute("error", error);
        return "calculadora.jsp";
    }
}
