#include <Magick++.h>
#include <iostream>

using namespace std;

static Magick::Image *letras[256];

Magick::Image conversao(string palavra){

    int tam = palavra.length();
    Magick::Image *palavra_braille[tam];

    for(int i=0; i<tam; i++){
        palavra_braille[i] = letras[palavra[i]];
    }

    Magick::Image palavra_final(Magick::Geometry(0, 0), Magick::Color("transparent"));

    int width = palavra_final.columns(), espaco = palavra_final.columns();

    for(int i=0; i<tam; i++){
        width = palavra_final.columns();
        if(i < tam-1){
            palavra_final.extent(Magick::Geometry(palavra_braille[i]->columns() + width + 30 , max(palavra_braille[i]->rows(), palavra_final.rows())), Magick::Color("transparent"));
        }else{
            palavra_final.extent(Magick::Geometry(palavra_braille[i]->columns() + width, max(palavra_braille[i]->rows(), palavra_final.rows())), Magick::Color("transparent"));
        }
        palavra_final.composite(*palavra_braille[i], width, 0, Magick::OverCompositeOp);
    }

    return palavra_final;

}

int main(){
    Magick::InitializeMagick("");

    letras[97] = new Magick::Image("Symbols/a.png");
    letras[98] = new Magick::Image("Symbols/b.png");
    letras[99] = new Magick::Image("Symbols/c.png");
    letras[100] = new Magick::Image("Symbols/d.png");
    letras[101] = new Magick::Image("Symbols/e.png");
    letras[102] = new Magick::Image("Symbols/f.png");
    letras[103] = new Magick::Image("Symbols/g.png");
    letras[104] = new Magick::Image("Symbols/h.png");
    letras[105] = new Magick::Image("Symbols/i.png");
    letras[106] = new Magick::Image("Symbols/j.png");
    letras[107] = new Magick::Image("Symbols/k.png");
    letras[108] = new Magick::Image("Symbols/l.png");
    letras[109] = new Magick::Image("Symbols/m.png");
    letras[110] = new Magick::Image("Symbols/n.png");
    letras[111] = new Magick::Image("Symbols/o.png");
    letras[112] = new Magick::Image("Symbols/p.png");
    letras[113] = new Magick::Image("Symbols/q.png");
    letras[114] = new Magick::Image("Symbols/r.png");
    letras[115] = new Magick::Image("Symbols/s.png");
    letras[116] = new Magick::Image("Symbols/t.png");
    letras[117] = new Magick::Image("Symbols/u.png");
    letras[118] = new Magick::Image("Symbols/v.png");
    letras[119] = new Magick::Image("Symbols/w.png");
    letras[120] = new Magick::Image("Symbols/x.png");
    letras[121] = new Magick::Image("Symbols/y.png");
    letras[122] = new Magick::Image("Symbols/z.png");
    letras[135] = new Magick::Image("Symbols/ç.png");


    string name, palavra;
    
    system("mkdir imgs");
    cout << "Digite o nome do arquivo: ";
    cin >> name;
    cout << "Digite a palavra para traduzir: ";
    cin >> palavra;

    conversao(palavra).write("imgs/"+name+".png");
    

    return 0;
}