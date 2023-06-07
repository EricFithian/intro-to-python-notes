class User {
    constructor(name) {
        this.name = name
    }

    greet() {
        return console.log(`Nice to meet you, ${this.name}`)
    }
}

const chris = new User("Chris");
console.log(chris.name);
chris.greet();