package com.example.eureka;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


public class search_page extends AppCompatActivity implements View.OnClickListener{
    private EditText editText;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search_page);
        Button advanced = (Button) findViewById(R.id.advanced);
        Button search = (Button) findViewById(R.id.search);
        editText = (EditText) findViewById(R.id.edit_text);
        advanced.setOnClickListener(this);
        search.setOnClickListener(this);

    }

    @Override
    public void onClick(View v){
        switch (v.getId()){
            case R.id.search:
                String inputText = editText.getText().toString();
               Toast.makeText(search_page.this,inputText,Toast.LENGTH_SHORT).show();
                break;
            case R.id.advanced:
                Intent intent = new Intent(search_page.this, advanceed_search_page.class);
                startActivity(intent);
                break;
            default:
                    break;
        }
    }
}
