# desafio1<br>
GO CHECK é uma startup de Ponto Eletronico Digital, visando facilitar, agilizar e fornecer uma transparência tanto para o colaborador quanto para a empresa. No dia a dia, é comum as pessoas esquecerem de registrarem o ponto ou registrarem incorretamente. Para esses casos, go check conta com o sistema de solictações de alterações, em que usuário deve verificar sua folha e solicitar as devidas correções. 
Pensando nisso, você como desenvolvedor deve criar um algoritmo que verifique a jornada do dia do colaborador e sugira as alterações para deixar tudo certinho.<br>
Você irá receber: Tipo de Registro - Horário<br>
Exemplo:
<br>
Jornada esperada Dia 1<br>
1 - 07:00:00<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Pontos realizado pelo colaborador<br>
Dia 1<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Jornada esperada Dia 2<br>
1 - 07:00:00<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Pontos realizado pelo colaborador<br>
Dia 2<br>
2 - 07:00:00<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Jornada esperada Dia 3<br>
1 - 07:00:00<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Pontos realizado pelo colaborador<br>
Dia 3<br>
2 - 07:15:00<br>
2 - 11:40:00<br>
2 - 11:40:20<br>
2 - 12:10:00<br>
2 - 17:34:00<br>

Jornada esperada Dia 4<br>
1 - 07:00:00<br>
2 - 11:00:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Pontos realizado pelo colaborador<br>
Dia 4<br>
2 - 07:13:00<br>
2 - 17:50:00<br>

Jornada esperada Dia 5<br>
1 - 07:00:00<br>
2 - 11:10:00<br>
2 - 12:00:00<br>
3 - 17:00:00<br>

Pontos realizado pelo colaborador<br>
Dia 5<br>
1 - 07:13:00<br>
2 - 11:10:00<br>
2 - 12:00:00<br>

Você deve produzir como saída as sugestões de registros. Podem ser exclusões, alterações ou inclusões <br>
Exemplo de saída<br>
07:00:00 - "adicionar"<br>
08:00:00 - "excluir"<br>
09:00:00 - "alterar"<br>
