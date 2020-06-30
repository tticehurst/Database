package com;

import com.sample.model.FoodType;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by kasun on 5/24/17.
 */
public class FoodService {

    public List getAvailableBrands(FoodType type){

        List brands = new ArrayList();

        if(type.equals(FoodType.BREAD)){
            brands.add("Adrianna Vineyard");
            brands.add(("J. P. Chenet"));

        }else if(type.equals(FoodType.CHEESE)){
            brands.add("Glenfiddich");
            brands.add("Johnnie Walker");

        }else if(type.equals(FoodType.PIZZA)){
            brands.add("Corona");

        }else {
            brands.add("No Brand Available");
        }
        return brands;
    }
}
