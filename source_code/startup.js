describe('General', function() {
      it('Startup', function() {
          cy.visit('https://programadorwebvalencia.com/cursos/testing/e2e/');
          cy.get('h1').contains('Testing End-to-End (E2E)');
          cy.get('.aside li').should('have.length', 7);
      })
})
