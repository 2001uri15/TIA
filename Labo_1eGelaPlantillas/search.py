# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from abc import ABC, abstractmethod

import util


class SearchProblem(ABC):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    @abstractmethod
    def getStartState(self):
        """
        Returns the start state for the search problem.
        Devuelve el estado inicial del problema de búsqueda.
        """
        util.raiseNotDefined()

    @abstractmethod
    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        Devuelve Verdadero si y solo si el estado es un estado objetivo válido.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.

        Estado: Estado de búsqueda

        Para un estado dado, esto debería devolver una lista de tripletas (sucesor, acción, coste de paso),
        donde «sucesor» es un sucesor del estado actual, «acción» es la acción necesaria para llegar a él
        y «costo de paso» es el coste incremental de la expansión a ese sucesor.
        """
        util.raiseNotDefined()

    @abstractmethod
    def getCostOfActions(self, actions):
        """
         acciones: Una lista de acciones a realizar.

        Este método devuelve el coste total de una secuencia específica de acciones.
        La secuencia debe estar compuesta de movimientos válidos.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    estadoIni = problem.getStartState()
    sucesores = util.Stack() # Declaramos la variable de los sucesores como una pila
    visitados = set() # Conjunto de posiciones visitados; No se pueden repetirr
    posAct = estadoIni # Posición actual

    # y ponerlo así
    sucesores.push((posAct, []))
    while not sucesores.isEmpty():
        posAct, direcciones = sucesores.pop()  # siguiente estado, accion (norte, sur, este, oeste)
        if problem.isGoalState(posAct):
            return direcciones # Debolvemos el recorrido si es a donde queremos llegar
        visitados.add(posAct)  # Añadimos al conjunto las casillas visitadas
        for sucesor in problem.getSuccessors(posAct):
            if sucesor[0] not in visitados:
                direccion = sucesor[1]
                faltante = direcciones + [direccion]
                sucesores.push((sucesor[0], faltante))

    return None







def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    estadoIni = problem.getStartState()
    sucesores = util.Queue()
    visitadas = set()
    direcciones = []
    nodoAct = estadoIni

    for sucesor in problem.getSuccessors(nodoAct):
        direccion = sucesor[1]
        hastaLlegar = direcciones + [direccion]
        sucesores.push((sucesor[0], hastaLlegar))

    while not problem.isGoalState(nodoAct) and not sucesores.isEmpty():
        nodoAct, direcciones = sucesores.pop()
        visitadas.add(nodoAct)
        for sucesor in problem.getSuccessors(nodoAct):
            if sucesor[0] not in visitadas:
                direccion = sucesor[1]
                hastaLlegar = direcciones + [direccion]
                sucesores.push((sucesor[0], hastaLlegar))

    if sucesores.isEmpty and not problem.isGoalState(nodoAct):
        direcciones = None

    print(direcciones)

    return direcciones
    
    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    inic = problem.getStartState()
    sucesores = util.PriorityQueue()
    visitados = set()
    posAct = inic

    # y ponerlo así
    sucesores.push((posAct, []), 0)
    while not sucesores.isEmpty():
        posAct, direcciones = sucesores.pop()  # siguiente estado, accion (norte, sur, este, oeste)
        if problem.isGoalState(posAct):
            return direcciones
        visitados.add(posAct)  # Añadimos al conjunto las casillas visitadas
        for sucesor in problem.getSuccessors(posAct):
            if sucesor[0] not in visitados:
                visitados.add(sucesor[0])  # Si no introducimos esta sentencia al recorre por nivel puede que algunos elementos se añadan dos veces a la cola
                # Esto sucede porque la cola es una estructura FIFO y al tener varios caminos puede que haya elementos que tienen los mismos sucesores
                direccion = sucesor[1]
                faltante = direcciones + [direccion]
                peso = problem.getCostOfActions(faltante)
                sucesores.push((sucesor[0], faltante), peso)  # El error está en que cada vez
    return None


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
