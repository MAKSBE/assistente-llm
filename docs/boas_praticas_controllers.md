# Boas Práticas em Controllers

- Controllers devem ser finos, delegar tudo para os services.
- Validações e lógica devem estar no service ou em validadores.
- Use os atributos `[HttpPost]`, `[HttpGet]`, `[FromBody]` corretamente.
- Sempre retorne `IActionResult` ou `ActionResult<T>`.

```csharp
[ApiController]
[Route("api/[controller]")]
public class UsuarioController : ControllerBase {
    private readonly IUsuarioService _service;

    public UsuarioController(IUsuarioService service) {
        _service = service;
    }

    [HttpPost]
    public async Task<IActionResult> Criar([FromBody] UsuarioDto dto) {
        var resultado = await _service.CriarAsync(dto);
        return Ok(resultado);
    }
}
