# Boas Práticas em Services

- Nunca acessar diretamente o banco de dados.
- Serviços devem ser orquestradores, não fazer validações detalhadas.
- Use injeção de dependência para repositórios e validadores.
- Divida responsabilidades por domínio.

Exemplo:

```csharp
public class UsuarioService : IUsuarioService {
    private readonly IUsuarioRepository _repo;

    public UsuarioService(IUsuarioRepository repo) {
        _repo = repo;
    }

    public async Task<UsuarioDto> CriarAsync(UsuarioDto dto) {
        var usuario = new Usuario(dto.Nome, dto.Email);
        await _repo.InserirAsync(usuario);
        return new UsuarioDto(usuario);
    }
}

