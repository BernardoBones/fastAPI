marca(volkswagen, polo, vermelho).
marca(volkswagen, gol, preto).
marca(volkswagen, jetta, branco).
marca(volkswagen, tiguan, azul).
marca(volkswagen, passat, cinza).
marca(volkswagen, golf, roxo).
marca(porsche, gt3-rs, vermelho).
marca(porsche, panamera, preto).
marca(porsche, carrera, branco).
marca(porsche, taycan, azul).
marca(porsche, cayman, cinza).
marca(porsche, macan, roxo).
marca(ferrari, 458, vermelho).
marca(ferrari, roma, preto).
marca(ferrari, 812, branco).
marca(ferrari, f40, azul).
marca(ferrari, purosangue, cinza).
marca(ferrari, sf90, roxo).
marca(lamborghini, aventador, vermelho).
marca(lamborghini, urus, preto).
marca(lamborghini, huracan, branco).
marca(lamborghini, diablo, azul).
marca(lamborghini, veneno, cinza).
marca(lamborghini, revuelto, roxo).

gosta(vinicius, volkswagen).
gosta(bernardo, volkswagen).
gosta(guilherme, volkswagen).
gosta(henrique, ferrari).
gosta(gregory, ferrari).
gosta(iury, ferrari).
gosta(pedro, lamborghini).
gosta(richardon, lamborghini).
gosta(andre, lamborguini).

gosta_cor(vinicius, branco).
gosta_cor(bernardo, azul).
gosta_cor(guilherme, preto).
gosta_cor(henrique, roxo).
gosta_cor(gregory, cinza).
gosta_cor(iury, branco).
gosta_cor(pedro, azul).
gosta_cor(richardson, preto).
gosta_cor(andre, preto).

gosta_carro_cor(Pessoa, Marca, Cor) :-gosta(Pessoa, Marca), gosta_cor(Pessoa, Cor).