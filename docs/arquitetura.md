# Arquitetura da Solução

A aplicação utiliza a arquitetura em camadas com os seguintes projetos:

- **Domain**: Contém entidades, interfaces e regras de negócio.
- **Application**: Camada responsável pelos serviços e casos de uso.
- **Infrastructure**: Implementação de interfaces como repositórios, serviços externos, cache etc.
- **API**: Interface de entrada da aplicação (controllers, middlewares).

A comunicação entre camadas deve ser feita exclusivamente via **interfaces**.

