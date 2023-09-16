# redis_django_celery

Comando usado para instalar o banco de dados em memoria redis no docker 
    
    docker run -p 6379:6379 redis/redis-stack:latest
 Este comando inicia o Celery Beat como um serviço separado. O Celery Beat é responsável
 por agendar tarefas em horários específicos. Ele executará as tarefas que você agendou de acordo com as configurações que você definiu.

     celery -A project beat -linfo
Este comando inicia um worker do Celery que executará as tarefas quando elas forem enfileiradas para execução.
O worker monitora a fila de tarefas e executa as tarefas à medida que elas são adicionadas à fila.

    celery -A project worker -l info


O Redis, em conjunto com o Celery, desempenha um papel fundamental na construção de sistemas de tarefas em 
segundo plano escaláveis e distribuídos em uma aplicação Django. Aqui estão as principais funções do Redis e do Celery em uma aplicação Django:

1-Celery:

    Execução de Tarefas em Segundo Plano: O Celery é um sistema de fila de tarefas em segundo plano que permite executar tarefas assíncronas em sua aplicação. 
    Isso é útil quando você precisa executar tarefas que podem demorar um tempo considerável para serem concluídas, como envio de e-mails, processamento de imagens, geração de relatórios, etc. 
    Em vez de esperar que essas tarefas sejam concluídas durante uma solicitação HTTP, você pode enfileirá-las para execução em segundo plano.
  
    Escalabilidade: O Celery é escalável, o que significa que você pode executar vários "workers" (trabalhadores) que podem processar tarefas em paralelo. 
    Isso é especialmente importante em aplicações de alto tráfego, onde muitas tarefas podem ser enfileiradas simultaneamente.
  
    Agendamento de Tarefas: O Celery inclui um componente chamado Celery Beat, que é um agendador de tarefas. 
    Ele permite que você agende tarefas para serem executadas em horários específicos ou em intervalos regulares.

2-Redis:

    Armazenamento de Fila de Tarefas: O Redis é um banco de dados de chave-valor extremamente rápido e eficiente que é frequentemente usado como o "broker" (gerenciador de fila) para o Celery.
    Ele armazena as tarefas enfileiradas em uma estrutura de dados chamada "lista" (list) ou "fila" (queue) no Redis.
    Isso permite que várias instâncias do Celery, em diferentes servidores ou contêineres, acessem a mesma fila de tarefas para processamento.
  
    Gerenciamento de Tarefas em Tempo Real: O Redis é conhecido por sua baixa latência e capacidade de manipulação de dados em tempo real. 
    Isso o torna ideal para o gerenciamento de tarefas em fila e também para outras funcionalidades em tempo real, como atualizações em tempo real de aplicativos da web.
  
  Em resumo, o Redis é usado como um meio para armazenar e gerenciar as tarefas enfileiradas pelo Celery em uma aplicação Django. Ele atua como um "broker" confiável que permite que as tarefas sejam distribuídas e processadas de forma assíncrona e escalável. O Celery, por sua vez, é o mecanismo que permite que você defina, enfileire e execute essas tarefas em segundo plano. Juntos, o Redis e o Celery tornam sua aplicação mais eficiente e escalável, permitindo que você execute tarefas demoradas sem afetar a capacidade de resposta de sua aplicação principal.

https://pypi.org/project/redis/
https://www.codingforentrepreneurs.com/blog/celery-redis-django/
https://www.codingforentrepreneurs.com/blog/redis-on-windows/
