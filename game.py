import pygame
import random
import time
import os
import math

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
# Definir área de coleta da mesa de entregas
DELIVERY_PICKUP_AREA = pygame.Rect(550, 1000, 300, 50)  # Define uma área retangular pequena dentro da mesa de entregas
ORDER_PICKUP_POSITION = (1041, 957)


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
        self.speed = 10
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

    # Modificar a função `pick_up_order` na classe `Character`
    def pick_up_order(self):
        # Verifique se a garçonete está na posição exata para pegar o pedido
        if self.rect.center == ORDER_PICKUP_POSITION:
            self.carrying_meal = True
            return True
        return False


    def deliver_order(self, customer):
        if self.carrying_meal:
            self.carrying_meal = None
            customer.received_order = True
            return True
        return False

    def attend_customer(self, customer):
        if customer.waiting_for_order and not customer.attended:
            customer.show_order = False  # Oculta o pedido até a garçonete chegar
            self.set_target(customer.rect.center)

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
        self.speed = 10
        self.is_moving = False
        self.attended = False
        self.in_queue = True
        self.received_order = False
        self.payment_timer = None
        self.mad = False
        self.payment_amount = 15
        self.show_order = False  # Novo atributo para controlar a exibição do pedido


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

        if self.received_order and not self.payment_timer:
            self.payment_timer = time.time() + random.uniform(3, 8)

        elif self.payment_timer and time.time() >= self.payment_timer:
            self.kill()

    def draw_order(self, screen):
        if self.show_order:  # Exibe apenas quando `show_order` está True
            screen.blit(self.order, (self.rect.centerx - self.order.get_width() // 2,
                                     self.rect.top - self.order.get_height()))
        
        if self.mad:
            screen.blit(MAD_CLIENT_IMAGE, (self.rect.centerx - MAD_CLIENT_IMAGE.get_width() // 2, self.rect.centery - MAD_CLIENT_IMAGE.get_height() // 2))

# Classe para a Mesa
class Table(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = TABLE_IMAGE
        self.rect = self.image.get_rect(center=(x, y))
        self.occupied = False  # Indica se a mesa está ocupada
        self.order_on_table = None  # Novo atributo para o pedido na mesa


# Carregar a imagem de fundo para a primeira fase
BACKGROUND_IMAGE = pygame.image.load("background_1.png").convert()

class Game:
    def __init__(self):
        self.character = Character(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
        # Definindo mesas com posições de entrega
        self.tables = [
            {"positions": [(538, 400), (913, 400)], "area": pygame.Rect(480, 350, 500, 100), "occupied": False, "delivery_position": (736, 465), "order_on_table": None, "order_position": (633, 318)},
            {"positions": [(1184, 400), (1560, 397)], "area": pygame.Rect(1100, 350, 500, 100), "occupied": False, "delivery_position": (1379, 475), "order_on_table": None, "order_position": (1281, 317)},
            {"positions": [(863, 611), (1237, 609)], "area": pygame.Rect(800, 550, 500, 120), "occupied": False, "delivery_position": (1057, 705), "order_on_table": None, "order_position": (963, 529)},
            {"positions": [(541, 888), (981, 888)], "area": pygame.Rect(480, 850, 500, 100), "occupied": False, "delivery_position": (727, 740), "order_on_table": None, "order_position": (633, 807)},
            {"positions": [(1186, 888), (1556, 888)], "area": pygame.Rect(1100, 850, 500, 100), "occupied": False, "delivery_position": (1368, 728), "order_on_table": None, "order_position": (1285, 805)}
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
        self.delivery_positions = []
        self.waitress_target_customer = None
        self.target_order_click = False  # Novo atributo para monitorar o estado de coleta
        self.target_customer_for_delivery = None  # Cliente que receberá o pedido


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
        self.score += customer.payment_amount
        customer.received_order = True

    def check_goal(self):
        if self.score >= self.goal:
            print("Meta alcançada! Fase concluída.")

    def run(self):
        running = True
        self.target_order_click = False  # Inicializa o estado do clique para pegar o pedido

        while running:
            screen.blit(BACKGROUND_IMAGE, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                     # Clique para pegar pedido pronto na mesa de entregas
                    if self.order_queue and self.delivery_positions:
                        order_position = self.delivery_positions[0]
                        order_rect = pygame.Rect(order_position[0], order_position[1], 50, 50)

                        if order_rect.collidepoint(pos):
                            print("Clique detectado na área do pedido")
                            self.character.set_target(ORDER_PICKUP_POSITION)
                            self.target_order_click = True

                    # Clique para entregar o pedido ao cliente (após pegar o pedido)
                    if self.character.carrying_meal:
                        for table in self.tables:
                            if table["area"].collidepoint(pos):
                                # Define o destino como a posição de entrega da mesa onde o cliente está
                                self.character.set_target(table["delivery_position"])
                                self.target_customer_for_delivery = next(
                                    (customer for customer in self.customers if customer.rect.colliderect(table["area"]) and customer.waiting_for_order),
                                    None
                                )
                                break


                    # Seleciona cliente na fila para se mover para uma mesa
                    for customer in self.customers:
                        if customer.rect.collidepoint(pos) and not customer.is_moving:
                            self.selected_customer = customer
                            break

                    # Se o cliente for selecionado, move-o para uma mesa disponível
                    if self.selected_customer:
                        for table in self.tables:
                            if not table["occupied"] and table["area"].collidepoint(pos):
                                self.selected_customer.set_target(table["positions"][0])
                                table["occupied"] = True
                                self.selected_customer = None
                                self.update_queue()
                                break

                    # Clique para registrar o pedido de um cliente sentado
                    for customer in self.customers:
                        if customer.waiting_for_order and not customer.attended:
                            customer.show_order = False  # Oculta o pedido até a garçonete chegar
                            for table in self.tables:
                                if table["area"].collidepoint(pos) and customer.rect.colliderect(table["area"]):
                                    # Move a garçonete para a `delivery_position` da mesa para registrar o pedido
                                    self.character.set_target(table["delivery_position"])
                                    self.waitress_target_customer = customer
                                    break

                     # Quando a garçonete atingir a posição de coleta e o pedido tiver sido clicado
                    if self.target_order_click and self.character.pick_up_order():
                        if self.order_queue:
                            # Retira o pedido da fila de entrega
                            self.order_queue.pop(0)
                            self.delivery_positions.pop(0)
                            self.target_order_click = False  # Resetar a ação de coleta

                            # Define o cliente de destino para entrega do pedido
                            for customer in self.customers:
                                if customer.waiting_for_order and not customer.received_order:
                                    self.character.set_target(customer.rect.center)
                                    self.target_customer_for_delivery = customer  # Marca o cliente para entrega
                                    break

                            # Renderizar o pedido acima do cliente quando estiver marcado para exibição
                            for customer in self.customers:
                                if customer.show_order:
                                    screen.blit(customer.order, (customer.rect.centerx - customer.order.get_width() // 2,
                                                                customer.rect.top - customer.order.get_height()))
                                            
                    

            # Verifica se a garçonete chegou ao cliente para entregar o pedido
            if hasattr(self, 'target_customer_for_delivery') and self.target_customer_for_delivery and self.character.deliver_order(self.target_customer_for_delivery):
                self.deliver_order_to_customer(self.target_customer_for_delivery)

                # Encontra a mesa associada ao cliente e coloca o pedido na mesa
                for table in self.tables:
                    if table["area"].colliderect(self.target_customer_for_delivery.rect):
                        table["order_on_table"] = self.target_customer_for_delivery.order  # Armazena o pedido na mesa
                        break

                self.target_customer_for_delivery = None  # Reseta o cliente de entrega após entregar o pedido
                self.character.carrying_meal = None

            # Verifica se a garçonete chegou ao cliente para anotar o pedido
            if self.waitress_target_customer and not self.character.target_pos:
                for table in self.tables:
                    if table["area"].colliderect(self.waitress_target_customer.rect):
                        # Define a posição de atendimento da garçonete
                        self.character.set_target(table["delivery_position"])
                        if self.character.rect.center == table["delivery_position"]:
                            self.waitress_target_customer.attended = True
                            self.waitress_target_customer.order_made = True
                            self.order_queue.append(self.waitress_target_customer.order)
                            self.order_ready_timer[self.waitress_target_customer.order] = time.time() + 9
                            self.waitress_target_customer.show_order = True  # Exibir o pedido acima do cliente
                            self.waitress_target_customer = None
                        break

            # Verifica se a garçonete alcançou a posição de coleta e o pedido foi clicado
            if self.target_order_click and self.character.pick_up_order():
                # Retira o pedido da fila de entrega e reseta o clique para pegar o pedido
                if self.order_queue:
                    self.order_queue.pop(0)
                    self.delivery_positions.pop(0)
                    self.target_order_click = False
                    # Define que a garçonete está carregando o pedido, mas aguarda o próximo clique na mesa
                    self.character.carrying_meal = True

            # Verifica se a garçonete chegou ao cliente para entregar o pedido
            if self.target_customer_for_delivery and self.character.rect.center == self.character.target_pos:
                self.deliver_order_to_customer(self.target_customer_for_delivery)
                self.target_customer_for_delivery = None  # Reseta o cliente de entrega após entregar o pedido
                self.character.carrying_meal = None  # Retira o item da garçonete  

            # Renderizar o pedido nas posições específicas da mesa
            for table in self.tables:
                if table.get("order_on_table") is not None:
                    screen.blit(table["order_on_table"], table["order_position"])

            # Remover clientes que saíram e liberar mesas
            for customer in self.customers:
                if customer.payment_timer and time.time() >= customer.payment_timer:
                    # Encontre a mesa onde o cliente estava e marque-a como desocupada
                    for table in self.tables:
                        if table["area"].colliderect(customer.rect):
                            table["occupied"] = False
                            table["order_on_table"] = None  # Remove o pedido da mesa
                            break
                    customer.kill()  # Remove o cliente do jogo
            

            # Atualizar movimento da garçonete e dos clientes
            self.character.update()
            self.customers.update()
            self.spawn_customer()
            display_mouse_position()

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

    def update_orders_on_delivery_table(self):
        delivery_table_start_x = 1100
        delivery_table_y = 981
        current_time = time.time()
        
        ready_orders = [order for order in self.order_queue if current_time >= self.order_ready_timer.get(order, float('inf'))]
        self.delivery_positions = [(delivery_table_start_x - index * 100, delivery_table_y) for index, _ in enumerate(ready_orders)]

        # Exibir pedidos prontos na mesa de entrega
        for index, order in enumerate(ready_orders):
            screen.blit(order, self.delivery_positions[index])

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
