import pygame
import random
import time
import os

# Inicializando o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Restaurante dos Personagens")

# Definindo cores e variáveis
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 120

# Fonte para exibir texto
font = pygame.font.Font(None, 36)

# Função para carregar imagens com tratamento de erros
def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        try:
            img = pygame.image.load(os.path.join(folder_path, filename)).convert_alpha()
            images.append(img)
        except Exception as e:
            print(f"Erro ao carregar {filename}: {e}")
    return images

# Carregar imagens de pedidos e refeições
ORDERS = load_images_from_folder(os.path.join(os.getcwd(), "orders"))
MEALS = load_images_from_folder(os.path.join(os.getcwd(), "meals"))

# Verificar se há imagens suficientes para pedidos e refeições
if len(ORDERS) != len(MEALS):
    print("Aviso: O número de imagens de pedidos e refeições não é o mesmo.")

# Dicionário para associar cada refeição ao pedido correspondente
MEAL2ORDER = {MEALS[i]: ORDERS[i] for i in range(min(len(MEALS), len(ORDERS)))}

# Carregar imagens da garçonete e da mesa
WAITER_IMAGE = pygame.image.load("client.png").convert_alpha()  # Substitua por caminho correto
TABLE_IMAGE = pygame.image.load("empty_table.png").convert_alpha()    # Substitua por caminho correto

# Carregar imagens de tela de título e instruções
TITLE_IMAGE = pygame.image.load("start_game.png").convert()
INSTRUCTIONS_IMAGE = pygame.image.load("instructions.png").convert()
FIRST_IMAGE = pygame.image.load("primeira_pagina.png").convert()
SECOND_IMAGE = pygame.image.load("second_page.png").convert()
BACKGROUND_IMAGE = pygame.image.load("background_1.png").convert()

# Caminho das imagens do cliente
CLIENTE_EM_PE = pygame.image.load("client_pe.png").convert_alpha()   # Substitua pelo caminho correto
CLIENTE_SENTADO = pygame.image.load("cliente_sentado.png").convert_alpha()   # Substitua pelo caminho correto
MAD_CLIENT_IMAGE = pygame.image.load("mad_client.png").convert_alpha()

# Configuração da área da "mesa de entregas"
DELIVERY_TABLE_AREA = pygame.Rect(150, 981, 970, 98)

def get_centered_position(image):
    image_rect = image.get_rect()
    x = (SCREEN_WIDTH - image_rect.width) // 2
    y = (SCREEN_HEIGHT - image_rect.height) // 2
    return x, y

# Função para exibir a posição do mouse
def display_mouse_position():
    mouse_pos = pygame.mouse.get_pos()
    mouse_text = font.render(f"Mouse Position: {mouse_pos}", True, BLACK)
    screen.blit(mouse_text, (10, 10))

# Função para exibir a tela de título
def show_title_screen():
    title_x, title_y = get_centered_position(TITLE_IMAGE)

    title_running = True
    while title_running:
        screen.fill(BLACK)  # Limpa a tela a cada quadro
        screen.blit(TITLE_IMAGE, (title_x, title_y))  # Desenha a imagem do título centralizada

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Verifique se o clique foi na área de "Play"
                if 1560 < pos[0] < 1722 and 491 < pos[1] < 579:  # Ajuste essas coordenadas conforme necessário
                    title_running = False
                    return "play"
                # Verifique se o clique foi na área de "Instructions"
                elif 1375 < pos[0] < 1713 and 626 < pos[1] < 682:  # Ajuste essas coordenadas conforme necessário
                    show_instructions_screen()

        # Exibe a posição do mouse na tela
        display_mouse_position()
        
        pygame.display.flip()
        clock.tick(FPS)

# Função para exibir a tela de instruções
def show_first_screen():
    first_x, first_y = get_centered_position(FIRST_IMAGE)

    primeira_parte = True
    segunda_parte = False
    first_screen = True
    while first_screen:
        screen.fill(BLACK)  # Limpa a tela a cada quadro
        if segunda_parte:
            screen.blit(SECOND_IMAGE, (first_x, first_y))  # Desenha a imagem de instruções centralizada
        else: 
            screen.blit(FIRST_IMAGE, (first_x, first_y))  # Desenha a imagem de instruções centralizada


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Verifique se o clique foi na área de "Play"
                if 1554 < pos[0] < 1716 and 975 < pos[1] < 1058:  # Ajuste essas coordenadas conforme necessário
                    print(primeira_parte)
                    print(segunda_parte)
                    if primeira_parte: 
                        segunda_parte = True
                        primeira_parte = False
                    else:
                        first_screen = False                   
                        return "play"  # Indica que o jogador quer iniciar o jogo
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                first_screen = False

        # Exibe a posição do mouse na tela
        display_mouse_position()
        
        pygame.display.flip()
        clock.tick(FPS)


# Função para exibir a tela de instruções
def show_instructions_screen():
    instructions_x, instructions_y = get_centered_position(INSTRUCTIONS_IMAGE)

    instructions_running = True
    while instructions_running:
        screen.fill(BLACK)  # Limpa a tela a cada quadro
        screen.blit(INSTRUCTIONS_IMAGE, (instructions_x, instructions_y))  # Desenha a imagem de instruções centralizada

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Verifique se o clique foi na área de "Play"
                if 794 < pos[0] < 1122 and 972 < pos[1] < 1032:  # Ajuste essas coordenadas conforme necessário
                    return "play"  # Indica que o jogador quer iniciar o jogo
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                instructions_running = False

        # Exibe a posição do mouse na tela
        display_mouse_position()
        
        pygame.display.flip()
        clock.tick(FPS)

# Classe para a Garçonete
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = CLIENTE_EM_PE
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.target_pos = None
        self.carrying_meal = None

    def update(self):
        if self.target_pos:
            dx, dy = self.target_pos[0] - self.rect.centerx, self.target_pos[1] - self.rect.centery
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist > self.speed:
                dx, dy = dx / dist, dy / dist
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
            else:
                self.rect.center = self.target_pos
                self.target_pos = None

    def set_target(self, pos):
        self.target_pos = pos

    def attend_customer(self, customer):
        if customer.waiting_for_order and not customer.attended:
            self.set_target(customer.rect.center)  # Define o alvo da garçonete para a posição do cliente


class Customer(pygame.sprite.Sprite):
    def __init__(self, start_position, order_image):
        super().__init__()
        self.image_standing = CLIENTE_EM_PE
        self.image_sitting = CLIENTE_SENTADO
        self.image = self.image_standing
        self.rect = self.image.get_rect(center=start_position)
        self.waiting_for_order = False
        self.order = order_image
        self.target_position = None
        self.speed = 2
        self.is_moving = False
        self.attended = False
        self.in_queue = True
        self.received_order = False
        self.payment_timer = None  # Temporizador de pagamento após o recebimento do pedido
        self.mad = False  # Indica se o cliente está bravo
        self.payment_amount = 15  # Valor padrão de pagamento

    def set_target(self, target_position):
        self.target_position = target_position
        self.is_moving = True
        self.in_queue = False

    def update(self):
        if self.is_moving and self.target_position:
            dx, dy = self.target_position[0] - self.rect.centerx, self.target_position[1] - self.rect.centery
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist > self.speed:
                dx, dy = dx / dist, dy / dist
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed
            else:
                self.rect.center = self.target_position
                self.is_moving = False
                self.image = self.image_sitting
                self.waiting_for_order = True

        # Verifica o temporizador de pagamento e atualiza o status
        if self.received_order and not self.payment_timer:
            # Inicia o temporizador de pagamento com um tempo aleatório entre 3 e 8 segundos
            self.payment_timer = time.time() + random.uniform(3, 8)

        elif self.payment_timer and time.time() >= self.payment_timer:
            # Cliente paga e vai embora
            self.rect.center = (-100, -100)  # Movendo o cliente para fora da tela
            self.kill()  # Remove o cliente do jogo

    def draw_order(self, screen):
        # Exibe o pedido acima do cliente enquanto ele espera e até que o pedido seja entregue
        if self.waiting_for_order or self.attended:
            screen.blit(self.order, (self.rect.centerx - self.order.get_width() // 2,
                                     self.rect.top - self.order.get_height()))
        
        # Exibe a imagem do cliente bravo se ele estiver bravo
        if self.mad:
            screen.blit(MAD_CLIENT_IMAGE, (self.rect.centerx - MAD_CLIENT_IMAGE.get_width() // 2, self.rect.centery - MAD_CLIENT_IMAGE.get_height() // 2))


# Classe para a Mesa
class Table(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = TABLE_IMAGE
        self.rect = self.image.get_rect(center=(x, y))
        self.occupied = False  # Indica se a mesa está ocupada

# Carregar a imagem de fundo para a primeira fase
BACKGROUND_IMAGE = pygame.image.load("background_1.png").convert()

class Game:
    def __init__(self):
        self.delivered_orders = []
        self.character = Character(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Definindo mesas com áreas de clique e posições das cadeiras
        self.tables = [
            {"positions": [(538, 400), (913, 400)], "area": pygame.Rect(480, 350, 500, 100), "occupied": False},
            {"positions": [(1184, 400), (1560, 397)], "area": pygame.Rect(1100, 350, 500, 100), "occupied": False},
            {"positions": [(863, 611), (1237, 609)], "area": pygame.Rect(800, 550, 500, 120), "occupied": False},
            {"positions": [(541, 888), (981, 888)], "area": pygame.Rect(480, 850, 500, 100), "occupied": False},
            {"positions": [(1186, 888), (1556, 888)], "area": pygame.Rect(1100, 850, 500, 100), "occupied": False}
        ]
        
        self.queue_positions = [(528, 496), (550, 496), (500, 496), (450, 496), (400, 496)]
        
        self.customers = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.character)
        self.selected_customer = None
        self.score = 0
        self.goal = 150  # Meta da fase
        self.last_customer_time = time.time()
        self.order_queue = []
        self.order_ready_timer = {}
        self.waitress_target_customer = None  # Cliente atual para anotar o pedido

    def spawn_customer(self):
        if len(self.customers) < len(self.queue_positions) and time.time() - self.last_customer_time > 10:
            queue_position = self.queue_positions[len(self.customers)]
            order_image = random.choice(ORDERS)
            new_customer = Customer(queue_position, order_image)
            self.customers.add(new_customer)
            self.all_sprites.add(new_customer)
            self.last_customer_time = time.time()

    def deliver_order_to_customer(self, customer):
        wait_time = time.time() - self.order_ready_timer[customer.order]
        if wait_time > 5:
            customer.mad = True
            customer.payment_amount = 10
        else:
            customer.payment_amount = 15
        self.score += customer.payment_amount  # Atualiza o score com o valor do pagamento
        customer.received_order = True

    # Método para verificar o progresso da fase
    def check_goal(self):
        if self.score >= self.goal:
            print("Meta alcançada! Fase concluída.")
            # Implementar lógica de avanço de fase aqui, se desejado

    # No método `run` da classe `Game`, atualize a lógica para entregar o pedido ao cliente
    def run(self):
        running = True
        while running:
            # Desenhar o fundo na tela
            screen.blit(BACKGROUND_IMAGE, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Seleciona cliente na fila para se mover para uma mesa
                    for customer in self.customers:
                        if customer.rect.collidepoint(pos) and not customer.is_moving:
                            self.selected_customer = customer
                            break
                    
                    if self.selected_customer:
                        for table in self.tables:
                            if not table["occupied"] and table["area"].collidepoint(pos):
                                self.selected_customer.set_target(table["positions"][0])
                                table["occupied"] = True
                                self.selected_customer = None
                                self.update_queue()
                                break
                    
                    # Registrar pedido se o cliente já estiver sentado
                    for customer in self.customers:
                        if customer.waiting_for_order and not customer.attended:
                            for table in self.tables:
                                if table["area"].collidepoint(pos) and customer.rect.colliderect(table["area"]):
                                    self.waitress_target_customer = customer
                                    self.character.attend_customer(customer)
                                    break
                    
                    # Detectar e pegar pedido na mesa de entrega
                    delivery_table_start_x = 1100  # Coordenada X inicial da mesa de entrega
                    delivery_table_y = 981  # Coordenada Y da mesa de entrega
                    for index, order in enumerate(self.delivered_orders):
                        order_position = pygame.Rect(delivery_table_start_x - index * 100, delivery_table_y, order.get_width(), order.get_height())
                        if order_position.collidepoint(pos) and not self.character.carrying_meal:
                            # Mover a garçonete até o pedido
                            self.character.set_target((order_position.centerx, order_position.centery))
                            self.character.carrying_meal = order  # A garçonete começa a carregar o pedido
                            self.delivered_orders.pop(index)  # Remove o pedido da mesa de entregas
                            break

                    # Entregar o pedido ao cliente quando clicar na mesa
                    if self.character.carrying_meal:
                        for table in self.tables:
                            if table["area"].collidepoint(pos):
                                for customer in self.customers:
                                    if customer.rect.colliderect(table["area"]) and customer.waiting_for_order:
                                        self.character.set_target(customer.rect.center)
                                        self.deliver_order_to_customer(customer)  # Atualiza o cliente e score
                                        table["occupied"] = False
                                        self.character.carrying_meal = None
                                        self.check_goal()
                                        break

            # Atualizar movimento da garçonete e dos clientes
            self.character.update()
            self.customers.update()
            self.spawn_customer()

            # Verifica se a garçonete alcançou o cliente para anotar o pedido
            if self.waitress_target_customer and not self.character.target_pos:
                self.waitress_target_customer.attended = True
                self.waitress_target_customer.order_made = True
                self.order_queue.append(self.waitress_target_customer.order)
                self.order_ready_timer[self.waitress_target_customer.order] = time.time() + 9
                self.waitress_target_customer = None

            # Atualizar e desenhar os pedidos na mesa de entrega
            self.update_orders_on_delivery_table()
            self.all_sprites.draw(screen)

            # Desenhar pedidos na mesa dos clientes
            for customer in self.customers:
                customer.draw_order(screen)

            # Exibir pontuação
            self.show_score()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

    def show_score(self):
        score_text = font.render(f"Pontuação: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 40))

    # Modifique o método update_orders_on_delivery_table para usar delivered_orders
    def update_orders_on_delivery_table(self):
        # Definir posição inicial da mesa de entregas
        delivery_table_start_x = 1100
        delivery_table_y = 981
        current_time = time.time()
        
        # Mover pedidos prontos de order_queue para delivered_orders
        for order in list(self.order_queue):  # Criamos uma cópia com list() para iterar
            if current_time >= self.order_ready_timer.get(order, float('inf')):
                self.delivered_orders.append(order)
                self.order_queue.remove(order)  # Remover o pedido de order_queue
        
        # Exibir todos os pedidos na mesa de entregas da direita para a esquerda
        for index, order in enumerate(self.delivered_orders):
            screen.blit(order, (delivery_table_start_x - index * 100, delivery_table_y))


    def update_queue(self):
        queue_index = 0
        for customer in self.customers:
            if customer.in_queue:
                customer.rect.center = self.queue_positions[queue_index]
                queue_index += 1

# Executando o jogo
if __name__ == "__main__":
    resultado = show_title_screen()
    if resultado == "play":
        resultado = show_first_screen()
    if resultado == "play":
        Game().run()
