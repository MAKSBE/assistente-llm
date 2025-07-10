# Padrão de DTOs

- DTOs representam dados de entrada/saída da API.
- Nunca retorne entidades diretamente.
- Separe DTOs de entrada e de resposta quando necessário.

```csharp
public class CriarUsuarioDto {
    public string Nome { get; set; }
    public string Email { get; set; }
}

public class UsuarioRespostaDto {
    public Guid Id { get; set; }
    public string Nome { get; set; }
}
