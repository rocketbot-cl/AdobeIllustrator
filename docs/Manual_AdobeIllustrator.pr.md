# Adobe Illustrator
  
Modulo para automatizar tarefas no Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Abrir Illustrator
  
Este comando permite abrir o programa Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do programa|Caminho do programa Adobe Illustrator.exe|C:/Program Files/Adobe/Adobe Illustrator CC 2019/Support Files/Contents/Windows/Illustrator.exe|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o programa abriu corretamente|variável|

### Abrir arquivo AutoCAD
  
Este comando permite abrir um arquivo AutoCAD no Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo|Caminho do arquivo que você deseja abrir no Adobe Illustrator|C:/Users/Usuário/Desktop/imagem.dxf|
|Opção de escala global|Selecione uma opção de escala global|Tamanho original|
|Unidades|Unidades do arquivo|1|
|Unidade de medida|Selecione a unidade de medida do arquivo|Centimeters|
|Escala global (porcentagem)|Escala global em porcentagem|100|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o arquivo foi aberto corretamente|variável|

### Alterar o modo de cor do documento
  
Este comando permite alterar o modo de cor do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Modo de cor|Modo de cor que deseja aplicar ao documento atual do Adobe Illustrator|RGB|

### Excluir camada
  
Este comando permite excluir uma camada do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da camada|Nome da camada que você deseja excluir do documento atual do Adobe Illustrator|Camada 1|

### Selecione a camada
  
Este comando permite selecionar uma camada do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Camada para selecionar|Nome da camada que você deseja selecionar do documento atual do Adobe Illustrator|Camada 1|

### Salvar .ai
  
Este comando permite salvar um arquivo do Adobe Illustrator no formato .ai
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho e nome do arquivo a salvar|Caminho e nome do arquivo a salvar. O caminho deve existir|C:/Users/usuario/Desktop/imagem.ai|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o arquivo foi salvo corretamente|variável|

### Fechar Illustrator
  
Este comando permite fechar o programa Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o programa fechou corretamente|variável|
