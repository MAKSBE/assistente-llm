# Padrões para Controllers

Controllers devem seguir a convenção `EntidadeController` e injetar os serviços via `IEntidadeService`.

Exemplo:

```csharp
[ApiController]
[Route("api/[controller]")]
public class UsuarioController : ControllerBase {
    private readonly IUsuarioService _service;

    public UsuarioController(IUsuarioService service) {
        _service = service;
    }

    [HttpPost]
    public async Task<IActionResult> Criar(UsuarioDto dto) {
        var result = await _service.Criar(dto);
        return Ok(result);
    }
}

