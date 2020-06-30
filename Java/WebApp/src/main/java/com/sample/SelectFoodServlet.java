package com.sample;

import com.sample.model.FoodType;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;


@WebServlet(
        name = "selectfoodservlet",
        name = "selectfoodservlet",
        urlPatterns = "/SelectFood"
)
public class SelectFoodServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        String FoodType = req.getParameter("Type");

        FoodService FoodService = new FoodService();
        FoodType l = FoodType.valueOf(FoodType);

        List FoodBrands = FoodService.getAvailableBrands(l);

        req.setAttribute("brands", FoodBrands);
        RequestDispatcher view = req.getRequestDispatcher("result.jsp");
        view.forward(req, resp);

    }
}
