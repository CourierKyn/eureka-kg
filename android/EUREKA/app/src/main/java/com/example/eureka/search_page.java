package com.example.eureka;

import android.content.Intent;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;


public class search_page extends AppCompatActivity implements View.OnClickListener{
    private EditText editText;
    private String[] data={"Apple", "Banana","Orange","WaterMelon","Pear","Grape","Pineapple",
    "Cherry","Mango","Apple", "Banana","Orange","WaterMelon","Pear","Grape","Pineapple",
            "Cherry","Mango"};
    private List<Fruit> fruitList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search_page);
        ActionBar actionBar = getSupportActionBar();
        if (actionBar !=null) {
            actionBar.hide();
        }
        Button advanced = (Button) findViewById(R.id.advanced);
        Button search = (Button) findViewById(R.id.search);
        editText = (EditText) findViewById(R.id.edit_text);
        advanced.setOnClickListener(this);
        search.setOnClickListener(this);
        //ArrayAdapter<String> adapter=new ArrayAdapter<String>(
          //      search_page.this,android.R.layout.simple_list_item_1,data);

        //ListView
        //初始化水果数据，例子
        initFruits();
        FruitAdapter adapter;
        adapter = new FruitAdapter(search_page.this,R.layout.fruit_item,fruitList);
        ListView listView = (ListView) findViewById(R.id.list_view);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Fruit fruit = fruitList.get(position);
                Toast.makeText(search_page.this,fruit.getName(),Toast.LENGTH_SHORT).show();
            }
        });
        //ListView

    }
    //ListView,使用水果实例
    private void initFruits(){
        for (int i = 0; i<2; i++){
            Fruit apple = new Fruit("Apple",R.drawable.img_1);
            fruitList.add(apple);
            Fruit banana = new Fruit("Banana",R.drawable.img_1);
            fruitList.add(banana);
            Fruit orange = new Fruit("Orange",R.drawable.img_1);
            fruitList.add(orange);
            Fruit watermelon = new Fruit("Watermelon",R.drawable.img_1);
            fruitList.add(watermelon);
            Fruit pear = new Fruit("Pear",R.drawable.img_1);
            fruitList.add(pear);
            Fruit grape = new Fruit("Grape",R.drawable.img_1);
            fruitList.add(grape);
            Fruit cherry = new Fruit("Cherry",R.drawable.img_1);
            fruitList.add(cherry);
            Fruit mango = new Fruit("Mango",R.drawable.img_1);
            fruitList.add(mango);
        }
    }
    //ListView,使用水果实例

    @Override
    public void onClick(View v){
        switch (v.getId()){
            //输入框事件
            case R.id.search:
                String inputText = editText.getText().toString();
               Toast.makeText(search_page.this,inputText,Toast.LENGTH_SHORT).show();
                break;
                //高级搜索页面
            case R.id.advanced:
                Intent intent = new Intent(search_page.this, advanceed_search_page.class);
                startActivity(intent);
                break;
            default:
                    break;
        }
    }
}
