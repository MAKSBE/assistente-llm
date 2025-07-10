# Validações com FluentValidation

Validações devem ser feitas com FluentValidation na camada Application.

```csharp
public class UsuarioDtoValidator : AbstractValidator<UsuarioDto> {
    public UsuarioDtoValidator() {
        RuleFor(x => x.Nome).NotEmpty().WithMessage("Nome é obrigatório");
        RuleFor(x => x.Email).EmailAddress().WithMessage("E-mail inválido");
    }
}
