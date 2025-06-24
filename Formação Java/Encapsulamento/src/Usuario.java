public class Usuario {
    private String senha;

    public Usuario(String senha) {
        this.senha = senha;
    }

    public void setSenha(String senhaTestada, String senhaNova) {
        if (senha.equals(senhaTestada)){
            this.senha = senhaNova;
            System.out.println("Senha alterada com sucesso!");
        }
        else{
            System.out.println("Senha atual incorreta. A senha não foi alterada.");
        }
    }
}
